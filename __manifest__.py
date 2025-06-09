{
    "name": "User Default POS Only",
    "version": "1.0",
    "summary": "Asigna solo grupo POS a nuevos usuarios y evita accesos no deseados",
    "author": "SGV Digital",
    "depends": ["base", "point_of_sale"],
    "data": [
        "data/default_user_group.xml",
        "data/hide_extra_menus.xml",
        "security/user_pos_rule.xml",
        "security/ir.model.access.csv"
    ],
    "installable": True,
    "application": False
}