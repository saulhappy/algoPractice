template = {
    "id": 4,
    "name": "sauls_template",
    "description": "Example checklist **is** a description.",
    "version": "1.0.1",
    "categories": [
        "safety",
        "example"
    ],
    "type": "PROJECT",
    "state": "DRAFT",
    "schema_version": 2,
    "default_actions": [
        "*"
    ],
    "definitions": [
        "a definition"
    ],
    "sections": [
        {
            "key": "all_features_test",
            "label": "All features test",
            "lines": [
                {
                    "key": "customer",
                    "label": "Customer",
                    "line_type": "text",
                    "actions_on": [
                        "camera",
                        "gallery"
                    ],
                    "actions_off": [
                        "notes"
                    ],
                    "description": "Do something here."
                },
                {
                    "key": "location",
                    "label": "Location",
                    "line_type": "text",
                    "actions_on": [],
                    "actions_off": [],
                    "description": None
                },
                {
                    "key": "turbine",
                    "label": "Turbine",
                    "line_type": "text",
                    "actions_on": [],
                    "actions_off": [],
                    "description": None
                },
                {
                    "key": "equipment_oem",
                    "label": "Equipment OEM",
                    "line_type": "text",
                    "actions_on": [
                        "camera",
                        "gallery"
                    ],
                    "actions_off": [],
                    "description": None
                },
                {
                    "key": "d_ring_rigging_eye",
                    "label": "D-Ring Rigging Eye",
                    "choices": [
                        {
                            "label": "",
                            "value": ""
                        },
                        {
                            "label": "Pass",
                            "value": "Pass"
                        },
                        {
                            "label": "Fail",
                            "value": "Fail"
                        },
                        {
                            "label": "N/A",
                            "value": "N/A"
                        }
                    ],
                    "line_type": "choice",
                    "actions_on": [],
                    "actions_off": [
                        "notes"
                    ],
                    "description": "**Special Instructions** Inspect the 1.25 D-ring Rigging eye2. "
                },
                {
                    "key": "broken_items",
                    "label": "Broken Items",
                    "choices": [
                        {
                            "label": "Thing 1",
                            "value": "Thing 1"
                        },
                        {
                            "label": "Thing 3",
                            "value": "Thing 3"
                        },
                        {
                            "label": "Thing 3",
                            "value": "Thing 3"
                        }
                    ],
                    "line_type": "multiple choice",
                    "actions_on": [],
                    "actions_off": [],
                    "description": None
                },
                {
                    "key": "image",
                    "label": "Image",
                    "line_type": "image",
                    "actions_on": [],
                    "actions_off": [],
                    "description": None
                },
                {
                    "key": "date_ended",
                    "label": "Date Ended",
                    "line_type": "date",
                    "actions_on": [],
                    "actions_off": [],
                    "description": "**Instructions** Enter the date in the following format (mm/dd/yyyy) "
                },
                {
                    "key": "this_is_a_really_long_string_of_text_we_want_to_put_into_this_report_n_n_its_really_great_to_be_working_on_this_project_loads_of_fun_is_being_had_by_all",
                    "label": "This is a really long string of text we want to put into this report.\\n\\n Its really great to be working on this project. **Loads of fun** is being had by all",
                    "line_type": "text block",
                    "actions_on": [],
                    "actions_off": [],
                    "description": None
                },
                {
                    "key": "sign_here",
                    "label": "Sign Here",
                    "line_type": "signature",
                    "actions_on": [],
                    "actions_off": [],
                    "description": None
                },
                {
                    "key": "select_vehicle_type",
                    "label": "Select Vehicle Type",
                    "choices": [
                        {
                            "label": "Chevorlet",
                            "value": "Chevorlet"
                        },
                        {
                            "label": "Ford",
                            "value": "Ford"
                        },
                        {
                            "label": "Tesla",
                            "value": "Tesla"
                        }
                    ],
                    "line_type": "choice",
                    "actions_on": [],
                    "actions_off": [],
                    "description": None
                }
            ],
            "description": "This is a long text. "
        },
        {
            "key": "another_section",
            "label": "Another Section",
            "lines": [
                {
                    "key": "alfa",
                    "label": "Alfa",
                    "line_type": "text",
                    "actions_on": [
                        "camera",
                        "gallery"
                    ],
                    "actions_off": [
                        "notes"
                    ],
                    "description": "Do something here."
                },
                {
                    "key": "bravo",
                    "label": "Bravo",
                    "line_type": "text",
                    "actions_on": [],
                    "actions_off": [],
                    "description": None
                },
                {
                    "key": "charlie",
                    "label": "Charlie",
                    "line_type": "text",
                    "actions_on": [],
                    "actions_off": [],
                    "description": None
                },
                {
                    "key": "delta",
                    "label": "Delta",
                    "line_type": "text",
                    "actions_on": [
                        "camera",
                        "gallery"
                    ],
                    "actions_off": [],
                    "description": None
                },
                {
                    "key": "eco",
                    "label": "Eco",
                    "choices": [
                        {
                            "label": "",
                            "value": ""
                        },
                        {
                            "label": "Pass",
                            "value": "Pass"
                        },
                        {
                            "label": "Fail",
                            "value": "Fail"
                        },
                        {
                            "label": "N/A",
                            "value": "N/A"
                        }
                    ],
                    "line_type": "choice",
                    "actions_on": [],
                    "actions_off": [
                        "notes"
                    ],
                    "description": "**Special Instructions** Inspect the 1.25 D-ring Rigging eye2. "
                },
                {
                    "key": "abc",
                    "label": "ABC",
                    "choices": [
                        {
                            "label": "A1",
                            "value": "A1"
                        },
                        {
                            "label": "B1",
                            "value": "B1"
                        }
                    ],
                    "line_type": "multiple choice",
                    "actions_on": [],
                    "actions_off": [],
                    "description": None
                },
                {
                    "key": "image",
                    "label": "Image",
                    "line_type": "image",
                    "actions_on": [],
                    "actions_off": [],
                    "description": None
                },
                {
                    "key": "date_ended",
                    "label": "Date Ended",
                    "line_type": "date",
                    "actions_on": [],
                    "actions_off": [],
                    "description": "**Instructions** Enter the date in the following format (mm/dd/yyyy) "
                },
                {
                    "key": "this_is_a_really_long_string_of_text_we_want_to_put_into_this_report_n_n_its_really_great_to_be_working_on_this_project_loads_of_fun_is_being_had_by_all",
                    "label": "This is a really long string of text we want to put into this report.\\n\\n Its really great to be working on this project. **Loads of fun** is being had by all",
                    "line_type": "text block",
                    "actions_on": [],
                    "actions_off": [],
                    "description": None
                },
                {
                    "key": "sign_here",
                    "label": "Sign Here",
                    "line_type": "signature",
                    "actions_on": [],
                    "actions_off": [],
                    "description": None
                },
                {
                    "key": "select_vehicle_type",
                    "label": "Select Vehicle Type",
                    "choices": [
                        {
                            "label": "Chevorlet",
                            "value": "Chevorlet"
                        },
                        {
                            "label": "Ford",
                            "value": "Ford"
                        },
                        {
                            "label": "Tesla",
                            "value": "Tesla"
                        }
                    ],
                    "line_type": "choice",
                    "actions_on": [],
                    "actions_off": [],
                    "description": None
                }
            ],
            "description": "This is a long text. "
        }
    ]
}

LINE_ITEM_ATTR_MAP = {
    "label": {
        "xls_col": "B",
        "xls_col_label": "Item Name",
        "json_attr": "display_text",
    },
    "line_type": {
        "xls_col": "C",
        "xls_col_label": "Type",
        "json_attr": "line_type",
    },
    "choices": {
        "xls_col": "D",
        "xls_col_label": "Choices (if applicable, separate with commas)",
        "json_attr": "choices",
    },
    "actions_on": {
        "xls_col": "E",
        "xls_col_label": "Accessories (on)",
        "json_attr": "actions_on",
    },
    "actions_off": {
        "xls_col": "F",
        "xls_col_label": "Accessories (off)",
        "json_attr": "actions_off",
    },
    "description": {
        "xls_col": "G",
        "xls_col_label": "Line Item description",
        "json_attr": "description_text",
    },  # Line Item Description ex: [title:Special Instructions] Inspect the 1.25 D-ring Rigging eye2.
    "image_source": {
        "xls_col": "H",
        "xls_col_label": "Image Source",
        "json_attr": "image_src",
    },
}
XLS_LINE_ITEM_COLS = [
    "label",
    "line_type",
    "choices",
    "actions_on",
    "actions_off",
    "description",
    "image_source",
]

actions_string = ""
actions_off = ["notes", "video", "safety"]


def print_test(arr):
    num = 5
    for action in arr:
        print(action)
    num += 1


print(print_test(actions_off))



