from database import SqliteDatabase

db = SqliteDatabase("user_data.db")


def update_data(userid, dataid, field, value):
    db.update_data(userid=userid, dataid=dataid, field=field, value=value)


update_data(1, 1, "type", "Computer")
