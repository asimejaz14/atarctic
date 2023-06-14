PRODUCT_SORTING_KEYS = {
    "index": "index",
    "created_at": "created_at",
    "customer_name": "customer_name",
    "tracking_number": "tracking_number",
    "updated_at": "updated_at",
    "status": "order_status",
}

PARTNER_SORTING_KEYS = {
    "index": "index",
    "created_at": "created_at",
    "customer_name": "customer_name",
    "tracking_number": "tracking_number",
    "updated_at": "updated_at",
    "status": "order_status",
}

STATUS = [
    (0, 'DELETED'),
    (1, 'ACTIVE'),
    (2, 'INACTIVE'),
    (3, 'BLOCKED'),
]


class Status:
    DELETED = 0
    ACTIVE = 1
    INACTIVE = 2


INQUIRY_SORTING_KEYS = {
    "name": "name",
    "email": "email",
    "created_at": "created_at",
    "updated_at": "updated_at",
    "assigned_to": "assigned_to",
}