#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
import subprocess
from pathlib import Path
from typing import Tuple

from pydantic import Field

from metagpt.actions.action import Action
from metagpt.logs import logger
from metagpt.schema import RunCodeContext, RunCodeResult
from metagpt.utils.exceptions import handle_exception
from llm_sandbox import SandboxSession
import os


class SetupSandbox(Action):
    name: str = "SetupSandbox"
    i_context: RunCodeContext = Field(default_factory=RunCodeContext)

    async def run(self, *args, **kwargs) -> RunCodeResult:
        sandbox_env = self.i_context.sandbox_env  # Get sandbox from environment
        if not sandbox_env:
            self.sandbox_env = SandboxSession(lang="python", keep_template=True)

        logger.info(f"Setting up sandbox for {' '.join(self.i_context.code_filename)}")
        working_directory = str(self.i_context.working_directory)

        # Install dependencies using sandbox
        await self._install_dependencies(working_directory, sandbox_env)

        # Copy files to sandbox
        for filename in os.listdir(working_directory):
            file_path = os.path.join(working_directory, filename)
            if os.path.isfile(file_path):
                sandbox_env.copy_to_runtime(file_path, f"/sandbox/{filename}")

        return RunCodeResult(summary="Sandbox setup complete", stdout="", stderr="")

    @staticmethod
    async def _install_dependencies(working_directory, sandbox_env: SandboxSession):
        req_path = Path(working_directory) / "requirements.txt"
        if not req_path.exists() or req_path.stat().st_size == 0:
            logger.warning(f"External dependencies not found {req_path}")
            return
        
        # Copy requirements.txt to sandbox
        sandbox_env.copy_to_runtime(str(req_path), "/sandbox/requirements.txt")
        
        # Install requirements in sandbox
        sandbox_env.execute_command("pip install -r /sandbox/requirements.txt")
        sandbox_env.execute_command("pip install pytest")  # Install pytest if needed