from django.core.management.base import BaseCommand
import subprocess
import sys


class Command(BaseCommand):
    help = "Run all commands"
    commands = [
        "python manage.py seed_connectivity", 
        "python manage.py seed_alert_types", 
        "python manage.py seed_enum"
    ]

    def handle(self, *args, **options):
        for command in self.commands:
            self.run_command(command)

    def run_command(self, command):
        model = command.split()[-1].replace("seed_", "")
        print(f"Inserting {model}")
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
        )
        stdout, _ = process.communicate()
        self.stdout.write(self.style.SUCCESS(stdout))
        if process.returncode != 0:
            sys.exit(f"Error: {stdout.strip()}")
