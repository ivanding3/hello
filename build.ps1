$reply = Read-Host "Do you want to build the project (y/n)"

if ($reply -eq "y") {
    python -m nuitka --standalone --windows-console-mode=disable --deployment --include-data-dir=assets=assets --include-data-files=map_objs.json=map_objs.json --python-flag=isolated,no_asserts,no_docstrings,no_warnings --main=main.py
    pause
} else {
    echo "Project will not be built."
}