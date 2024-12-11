from abc import ABC, abstractmethod


class ModelProvider(ABC):
    """Base class for AI model providers."""

    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        """Generate a response from the model."""
        pass

    @abstractmethod
    def get_capabilities(self) -> dict[str, any]:
        """Return provider capabilities."""
        pass


class DummyCloudProvider(ModelProvider):
    """Dummy implementation of a cloud AI provider."""

    def generate_response(self, prompt: str) -> str:
        return f"Dummy response to: {prompt}"

    def get_capabilities(self) -> dict[str, any]:
        return {
            "text_generation": True,
            "code_generation": True,
            "image_generation": False
        }
