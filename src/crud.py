from typing import Dict, List
from uuid import UUID


async def create(resource_payload: Dict) -> Dict:
    return {}


async def read(resource_id: UUID) -> Dict:
    return {}


async def read_all(filters: Dict = {}) -> List[Dict]:
    return []


async def update(resource_id: UUID, resource_payload: Dict) -> Dict:
    return {}


async def upsert(resource_id: UUID, resource_payload: Dict) -> Dict:
    return {}


async def delete(resource_id: UUID) -> Dict:
    return {}
