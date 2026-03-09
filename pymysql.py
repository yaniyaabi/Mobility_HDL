import streamlit as st
import pymssql


class OperationalError(Exception):
    pass


class err:
    OperationalError = OperationalError


def connect(*args, **kwargs):
    try:
        db = st.secrets["database"]
        return pymssql.connect(
            server=db["host"],
            user=db["user"],
            password=db["passwd"],
            database=db["db"],
            port=int(db.get("port", 1433)),
            login_timeout=30,
            timeout=30,
            as_dict=False,
        )
    except Exception as e:
        import traceback
        print("DB CONNECT ERROR:", repr(e))
        traceback.print_exc()
        raise OperationalError(str(e))
