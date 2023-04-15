from fastapi import APIRouter, Request, HTTPException
from modules.services.query_service import process_query

router = APIRouter()


@router.post("/get_dp_result")
async def get_dp_result(message: Request):
    try:
        req_info = await message.json()
        output = process_query(str(req_info['query']))
        return output
    except Exception as ex:
        print(ex)
        raise HTTPException(status_code=400, detail=str(ex))