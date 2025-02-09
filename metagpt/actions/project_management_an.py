#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/12/14 15:28
@Author  : alexanderwu
@File    : project_management_an.py
"""
from typing import List, Optional

from metagpt.actions.action_node import ActionNode

SHARED_KNOWLEDGE = ActionNode(
    key="Shared Knowledge",
    expected_type=str,
    instruction="Detail any shared knowledge, like common utility functions or configuration variables.",
    example="`api.js` contains shared utility functions for making API requests.",
)

REFINED_SHARED_KNOWLEDGE = ActionNode(
    key="Refined Shared Knowledge",
    expected_type=str,
    instruction="Update and expand shared knowledge to reflect any new elements introduced. This includes common "
    "utility functions, configuration variables for team collaboration. Retain content that is not related to "
    "incremental development but important for consistency and clarity.",
    example="`api.js` contains shared utility functions for making API requests.",
)

TASK_STEPS = ActionNode(
    key="Task Steps",
    expected_type=List[str],
    instruction="Break down the implementation approach into a step-by-step sequence of actions. "
    "Detail installation, setup, and implementation of all components from the original design. "
    "Be extremely specific in each step, including commands that need to be run, files that need to be created, "
    "and any other details that are necessary to successfully implement the project.",
    example=[
        "Step 1: Install Node.js (if not already installed). ",
        "Step 2: Create a new project folder. ",
        "Step 3: Initialize a new Node.js project using `npm init -y`. ",
        "Step 4: Install the Express framework using `npm install express`. ",
        "Step 5: Create a basic Express app by adding a simple route handler. ",
        "Step 6: Start the server and open it in your browser. ",
    ],
)

REFINED_TASK_STEPS = ActionNode(
    key="Refined Task Steps",
    expected_type=List[str],
    instruction="Review and refine the combined task list after the merger of Legacy Content and Incremental Content, "
    "and consistent with Refined File List. Ensure that tasks are organized in a logical and prioritized order, "
    "considering dependencies for a streamlined and efficient development process. ",
    example=[
        "Step 1: Install Node.js (if not already installed). ",
        "Step 2: Create a new project folder. ",
        "Step 3: Initialize a new Node.js project using `npm init -y`. ",
        "Step 4: Install the Express framework using `npm install express`. ",
        "Step 5: Create a basic Express app by adding a simple route handler. ",
        "Step 6: Start the server and open it in your browser. ",
    ],
)

ANYTHING_UNCLEAR_PM = ActionNode(
    key="Anything UNCLEAR",
    expected_type=str,
    instruction="Mention any unclear aspects in the project management context and try to clarify them.",
    example="Clarification needed on how to start and initialize third-party libraries.",
)

NODES = [
    SHARED_KNOWLEDGE,
    TASK_STEPS,
    ANYTHING_UNCLEAR_PM,
]

REFINED_NODES = [
    REFINED_SHARED_KNOWLEDGE,
    REFINED_TASK_STEPS,
    ANYTHING_UNCLEAR_PM,
]

PM_NODE = ActionNode.from_children("PM_NODE", NODES)
REFINED_PM_NODE = ActionNode.from_children("REFINED_PM_NODE", REFINED_NODES)
