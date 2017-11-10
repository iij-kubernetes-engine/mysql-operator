import logging

from .base import BaseCommand
from titanium.mysql import MysqlNode


class Command(BaseCommand):
    """This command will config the mysql."""
    def add_arguments(self, parser):
        pass

    def handle(self):
        logging.info("Start cloning.")
        node = MysqlNode()
        node.clone()
