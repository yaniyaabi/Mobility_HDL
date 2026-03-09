import streamlit as st
import pyodbc


class OperationalError(Exception):
    pass


class err:
    OperationalError = OperationalError


def connect(*args, **kwargs):
    try:
        db = st.secrets["database"]

        conn_str = (
            f"DRIVER={db['driver']};"
            f"SERVER={db['host']},{db['port']};"
            f"DATABASE={db['db']};"
            f"UID={db['user']};"
            f"PWD={db['passwd']};"
            f"Encrypt={db.get('encrypt', 'yes')};"
            f"TrustServerCertificate={db.get('trust_server_certificate', 'no')};"
        )
        return pyodbc.connect(conn_str)
    except Exception as e:
        raise OperationalError(str(e))
