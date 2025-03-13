import httpx
from django.utils.deprecation import MiddlewareMixin
import asyncio  # For running asynchronous tasks in synchronous code

class ExternalAPIMiddleware(MiddlewareMixin):
    def __call__(self, request):
        # Check if the request needs external API data
        if "data/" in request.path:
            try:
                # Run the async API call in a synchronous context
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                external_data = loop.run_until_complete(self.fetch_external_data())
                # Add the data to the request object
                request.external_api_data = external_data
            except Exception as e:
                # Handle errors
                request.external_api_data = {"error": str(e)}
        
        # Continue processing the request
        response = self.get_response(request)
        return response

    async def fetch_external_data(self):
        """Fetch data from the external API asynchronously."""
        async with httpx.AsyncClient() as client:
            response = await client.get("https://dog.ceo/api/breeds/image/random")
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": "Failed to fetch data"}
