# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Web Enterprise SHF',
    'category': 'Hidden',
    'version': '1.0',
    'description': """
Odoo Enterprise Web Client.
===========================

This module modifies the web addon to provide Enterprise design and responsiveness.
        """,
    'depends': ['web'],
    'auto_install': True,
    'data': [
        'views/partner_view.xml',
        'views/webclient_templates.xml',
    ],
    'assets': {
        'web.assets_qweb': [
            'shf_web_enterprise/static/src/**/*.xml',
        ],
        'web._assets_primary_variables': [
            ('prepend', 'shf_web_enterprise/static/src/legacy/scss/primary_variables.scss'),
        ],
        'web._assets_secondary_variables': [
            'shf_web_enterprise/static/src/legacy/scss/secondary_variables.scss',
        ],
        'web._assets_backend_helpers': [
            'shf_web_enterprise/static/src/legacy/scss/bootstrap_overridden.scss',
        ],
        'web._assets_common_styles': [
            ('replace', 'web/static/src/legacy/scss/ui_extra.scss', 'shf_web_enterprise/static/src/legacy/scss/ui.scss'),

            'shf_web_enterprise/static/fonts/fonts.scss',
        ],
        'web.assets_backend': [
            ('replace', 'web/static/src/webclient/webclient_extra.scss', 'shf_web_enterprise/static/src/webclient/webclient.scss'),
            ('replace', 'web/static/src/webclient/webclient_layout.scss', 'shf_web_enterprise/static/src/webclient/webclient_layout.scss'),

            ('replace', 'web/static/src/legacy/scss/dropdown_extra.scss', 'shf_web_enterprise/static/src/legacy/scss/fields.scss'),
            ('replace', 'web/static/src/legacy/scss/fields_extra.scss', 'shf_web_enterprise/static/src/legacy/scss/form_view.scss'),
            ('replace', 'web/static/src/legacy/scss/form_view_extra.scss', 'shf_web_enterprise/static/src/legacy/scss/list_view.scss'),
            ('replace', 'web/static/src/legacy/scss/list_view_extra.scss', 'shf_web_enterprise/static/src/legacy/scss/search_view.scss'),
            ('replace', 'web/static/src/search/search_panel/search_view_extra.scss', 'shf_web_enterprise/static/src/legacy/scss/dropdown.scss'),

            'shf_web_enterprise/static/src/legacy/scss/base_settings_mobile.scss',
            'shf_web_enterprise/static/src/legacy/scss/search_panel_mobile.scss',
            'shf_web_enterprise/static/src/legacy/scss/menu_search.scss',
            'shf_web_enterprise/static/src/legacy/scss/control_panel_layout.scss',
            'shf_web_enterprise/static/src/legacy/scss/control_panel_mobile.scss',
            'shf_web_enterprise/static/src/legacy/scss/kanban_view.scss',
            'shf_web_enterprise/static/src/legacy/scss/touch_device.scss',
            'shf_web_enterprise/static/src/legacy/scss/snackbar.scss',
            'shf_web_enterprise/static/src/legacy/scss/swipe_item_mixin.scss',
            'shf_web_enterprise/static/src/legacy/scss/form_view_mobile.scss',
            'shf_web_enterprise/static/src/legacy/scss/kanban_view_mobile.scss',
            'shf_web_enterprise/static/src/legacy/scss/modal_mobile.scss',
            'shf_web_enterprise/static/src/legacy/scss/promote_studio.scss',
            'shf_web_enterprise/static/src/legacy/scss/web_calendar_mobile.scss',
            'shf_web_enterprise/static/src/legacy/scss/barcodes_mobile.scss',
            'shf_web_enterprise/static/src/legacy/scss/pivot_view_mobile.scss',
            'shf_web_enterprise/static/src/search/**/*.scss',
            'shf_web_enterprise/static/src/webclient/**/*.scss',
            'shf_web_enterprise/static/src/views/**/*.scss',

            ('replace', 'web/static/src/legacy/js/fields/upgrade_fields.js', 'shf_web_enterprise/static/src/legacy/js/apps.js'),

            'shf_web_enterprise/static/src/search/**/*.js',
            'shf_web_enterprise/static/src/webclient/**/*.js',
            'shf_web_enterprise/static/src/views/**/*.js',

            'shf_web_enterprise/static/src/legacy/**/*.js',
            ("remove", "shf_web_enterprise/static/src/legacy/js/views/pivot_renderer.js"),
        ],
        "web.assets_backend_legacy_lazy": [
            "shf_web_enterprise/static/src/legacy/js/views/pivot_renderer.js",
        ],
        'web.assets_backend_prod_only': [
            ('replace', 'web/static/src/main.js', 'shf_web_enterprise/static/src/main.js'),
        ],
        'web.tests_assets': [
            'shf_web_enterprise/static/tests/*.js',
        ],
        'web.qunit_suite_tests': [
            ('remove', 'web/static/tests/legacy/fields/upgrade_fields_tests.js'),

            'shf_web_enterprise/static/tests/webclient/**/*.js',

            'shf_web_enterprise/static/tests/legacy/upgrade_fields_tests.js',
            'shf_web_enterprise/static/tests/legacy/views/list_tests.js',
            'shf_web_enterprise/static/tests/legacy/barcodes_tests.js',
        ],
        'web.qunit_mobile_suite_tests': [
            'shf_web_enterprise/static/tests/mobile/**/*.js',

            'shf_web_enterprise/static/tests/legacy/action_manager_mobile_tests.js',
            'shf_web_enterprise/static/tests/legacy/control_panel_mobile_tests.js',
            'shf_web_enterprise/static/tests/legacy/form_mobile_tests.js',
            'shf_web_enterprise/static/tests/legacy/relational_fields_mobile_tests.js',
            'shf_web_enterprise/static/tests/legacy/views/basic/basic_render_mobile_tests.js',
            'shf_web_enterprise/static/tests/legacy/views/calendar_mobile_tests.js',
            'shf_web_enterprise/static/tests/legacy/views/kanban_mobile_tests.js',
            'shf_web_enterprise/static/tests/legacy/views/list_mobile_tests.js',
            'shf_web_enterprise/static/tests/legacy/base_settings_mobile_tests.js',
            'shf_web_enterprise/static/tests/legacy/components/action_menus_mobile_tests.js',
            'shf_web_enterprise/static/tests/legacy/barcodes_mobile_tests.js',
        ],
    },
    'license': 'OEEL-1',
}
