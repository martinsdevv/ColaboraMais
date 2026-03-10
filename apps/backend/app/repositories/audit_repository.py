import json

from app.db.database import get_connection
from app.domain.audit_log import AuditLog


def create_log(log: AuditLog):

    conn = get_connection()

    conn.execute(
        """
        INSERT INTO audit_logs
        (user_id, action, entity, entity_id, data)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            log.user_id,
            log.action,
            log.entity,
            log.entity_id,
            json.dumps(log.data) if log.data else None
        )
    )

    conn.commit()