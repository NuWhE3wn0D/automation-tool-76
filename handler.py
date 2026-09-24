import logging

class DataHandler:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def validate_input(self, data: dict) -> bool:
        required_fields = {'id', 'payload', 'timestamp'}
        if not all(field in data for field in required_fields):
            return False
        if not isinstance(data['id'], int) or data['id'] < 0:
            return False
        return True

    def process_stream(self, data_stream: list):
        for entry in data_stream:
            try:
                if not self.validate_input(entry):
                    self.logger.warning(f"Invalid data packet: {entry}")
                    continue
                
                self._execute_task(entry)
            except Exception as e:
                self.logger.error(f"Processing failure: {e}")

    def _execute_task(self, data: dict):
        # core logic execution placeholder
        pass

if __name__ == "__main__":
    handler = DataHandler()
    stream = [{'id': 1, 'payload': 'test', 'timestamp': 12345}, {'id': -1}]
    handler.process_stream(stream)