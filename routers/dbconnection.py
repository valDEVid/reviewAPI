from fastapi import APIRouter, HTTPException
from db.schemas import schemas as sch
from db.db_config import get_dbconfig, try_dbconfig, write_dbconfig


router = APIRouter(tags=["Db Connection"])




# Get db config
@router.get("/dbconnection")
async def connection():
    config = get_dbconfig()
    if not try_dbconfig:
        raise {f"Exception {config}"}
    return {"Connection succesfully"}, config


# Post db config
@router.post("/dbconnection")
async def postconfig(user_config: sch.dbconn):
    config = write_dbconfig(user_config)
    if not try_dbconfig:
        raise {"Exception"}
    return HTTPException(status_code=200, detail="Connection Succesfully")