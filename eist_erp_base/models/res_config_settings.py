# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"


    # 应用
    module_eist_web_theme = fields.Boolean(string="Web Theme", default=False)
    module_eist_web_toolbox = fields.Boolean(string="Web ToolBox", default=False)
    module_eist_report_management = fields.Boolean(string="Report Management", default=False)


    hide_enterprise_app = fields.Boolean(
        string="Hide Enterprise App",
        default=False,
        config_parameter="eist_erp.hide_enterprise_app",
    )

    # 解决方案
    module_eist_pos = fields.Boolean(string="Solutions for stores and restaurants", default=False)

    # 扩展功能
    module_esit_geolocalize = fields.Boolean(string="Partners Geolocation", default=False)


    @api.onchange("hide_enterprise_app")
    def _onchange_hide_enterprise_app(self):
        """
        隐藏企业版应用
        """
        modules = self.env["ir.module.module"].search(
            ["&", ("to_buy", "=", True), ("application", "=", True)]
        )
        for module in modules:
            module.write({"application": not self.hide_enterprise_app})
        self.env["ir.module.module"].update_list()  # 避免打开设置页面报错


