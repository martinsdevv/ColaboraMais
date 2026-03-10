from app.repositories import audit_repository
from app.domain.audit_log import AuditLog


def log_action(user_id, action, entity, entity_id, data=None):

    log = AuditLog(
        user_id=user_id,
        action=action,
        entity=entity,
        entity_id=entity_id,
        data=data
    )

    audit_repository.create_log(log)