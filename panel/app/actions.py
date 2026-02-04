from __future__ import annotations

import logging
import os
import shutil
import subprocess
from pathlib import Path
from typing import Optional

from tkinter import messagebox


def ensure_logger(log_file: Path) -> logging.Logger:
    log_file.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("panel")
    if logger.handlers:
        return logger
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(log_file, encoding="utf-8")
    formatter = logging.Formatter("%(asctime)s %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def get_git_version(repo_root: Path) -> Optional[str]:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=repo_root,
            check=True,
            capture_output=True,
            text=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    return result.stdout.strip() or None


def log_start(logger: logging.Logger, version: Optional[str]) -> None:
    message = "start panel"
    if version:
        message = f"{message} [{version}]"
    logger.info(message)


def log_click(logger: logging.Logger, label: str) -> None:
    logger.info("klik: %s", label)


def handle_d_action(repo_root: Path, logger: logging.Logger) -> None:
    template_path = repo_root / "templates" / "DANE.docm"
    target_path = repo_root / "work" / "DANE_CURRENT.docm"

    try:
        if not template_path.exists():
            logger.error("D: brak szablonu %s", template_path)
            messagebox.showerror(
                "Brak szablonu",
                "Nie znaleziono templates\\DANE.docm.",
            )
            return

        if not target_path.exists():
            target_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(template_path, target_path)
            logger.info("D: utworzono plik %s", target_path)

        os.startfile(target_path)
        logger.info("D: otwarto plik %s", target_path)
    except Exception:
        logger.exception("D: blad podczas obslugi akcji")
