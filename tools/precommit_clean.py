#!/usr/bin/env python
"""
Pre-commit-Cleaner für das Repository.

Aktuell implementiert:
- Notebook-Outputs aus .ipynb entfernen (nbstripout)

Strukturell vorbereitet:
- weitere Ordner-/Dateibereinigungen können in clean_extra() ergänzt werden.
"""

from __future__ import annotations
import subprocess
import sys
from pathlib import Path
from typing import List

def log(msg: str) -> None:
    """Einfache Logfunktion für Ausgaben im Git-Hook-Kontext."""
    print(f"[precommit_clean] {msg}", file=sys.stderr)

def get_staged_files() -> List[Path]:
    """Liefert alle derzeit STAGED Dateien (für Commit vorgemerkt)."""
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=AM"],
        capture_output=True,
        text=True,
        check=True,
    )
    files = [Path(line) for line in result.stdout.splitlines() if line.strip()]
    log(f"{len(files)} Datei(en) im Index gefunden.")
    return files
def strip_notebook_outputs(files: List[Path]) -> int:
    """
    Entfernt Outputs aus allen .ipynb-Dateien in 'files' mit nbstripout und staged sie danach erneut.
    Gibt die Anzahl bearbeiteter Notebooks zurück.
    :param files:
    :return:
    """

    ipynbs = [f for f in files if f.suffix == ".ipynb"]
    if not ipynbs:
        log("Keine .ipynb-Dateien im Commit - nichts zu bereinigen.")
        return 0
    log(f"{len(ipynbs)}Notebooks(s) werden mit nbstripout bereinigt...")
    for nb in ipynbs:
        try:
            # nbstripout verändert die Datei IN PLACE
            subprocess.run(["nbstripout",str(nb)], check=True)
            # danach wieder zum Index hinzufügen, weil sich die Datei geändert hat
            subprocess.run(["git", "add", str(nb)], check=True)
            log(f"Bereinigt und erneut gestaged: {nb}")
        except FileNotFoundError:
            log(
                "Fehler: 'nbstripout' wurde nicht gefunden. "
                "Bitte im virtuellen Environment installieren: 'pip install nbstripout'."#

            )
            raise
        except subprocess.CalledProcessError as exc:
            log(f"Fehler beim Ausführen von nbstripout/git add für {nb}: {exc}")
            raise

    return len(ipynbs)

def clean_extra(files: List[Path]) -> int:
    """
    Platzhalter für Option C (später):
    - Aufräumen von bestimmten Ordnern
    - Löschen/ Bewegen unerwünschter Files
    - etc

    Aktuell: noch keine Aktion.
    :param files:
    :return:
    """

    # TODO: goodies hier implementieren. z.B. clean_inbox() , clean_tmp(), ...
    return 0

def main() -> int:
    try:
        files = get_staged_files()

        # Notebook- Output entfernen
        cleaned_notebooks = strip_notebook_outputs(files)

        # später hier grooming durchführen
        clean_extra(files)

        log(f"Fertig. {cleaned_notebooks} Notebooks(s) bereinigt.")
        return 0
    except Exception as exc:
        # Jede Exception führt zu einem Abbruch des Hooks
        log(f"Abbruch wegen Fehler: {exc}")
        return 1

    # TODO: hier prints/ Logging einbauen
    return 0

if __name__ == "__main__":
    raise SystemExit(main())