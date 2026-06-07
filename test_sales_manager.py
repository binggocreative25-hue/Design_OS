from memory.sales_manager import (
    SalesManager
)

manager = (
    SalesManager()
)

result = (
    manager.generate_strategy(
        "MFI"
    )
)

print(
    result.to_dict()
)