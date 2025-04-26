class BaseClient:
    def generate(self, prompt):
        raise NotImplementedError("Each client must implement the generate method.")

