# payload = {
#    "sec1":{
#       "line1":{
#          "notes":"Some Notes",
#          "value":"AA"
#       },
#       "line2":{
#          "value":"BB"
#       }
#    },
#    "sec2":{
#       "line1":{
#           "value": "",
#          "notes": "A note",
#          "media": ""
#       }
#    },
#    "sec3": {
#        "line1":{
#            "media": "media_file1.jpg",
#            "value": "123",
#            "notes": "notes"
#        }
#    }
# }

# payload = {
#    "sec1":{
#       "line1":{
#          "value":"AA",
#          "notes":"Some Notes"
#       }
#    },
#    "sec2": {
#        "line1": {
#            "value": "",
#            "notes": "",
#            "media": ""
#        }
#    }
# }


# payload = {
#    "another_section":{
#       "abc":{
#          "value":[
#             "A1"
#          ]
#       },
#       "eco":{
#          "value":"Pass"
#       },
#       "alfa":{
#          "value":"One"
#       },
#       "bravo":{
#          "value":"Two"
#       },
#       "charlie":{
#          "value":"chuck"
#       }
#    },
#    "all_features_test":{
#       "turbine":{
#          "value":""
#       },
#       "location":{
#          "value":""
#       }
#    }
# }


# template = {
#     "id": 4,
#     "name": "sauls_template",
#     "description": "Example checklist **is** a description.",
#     "version": "1.0.1",
#     "categories": [
#         "safety",
#         "example"
#     ],
#     "type": "PROJECT",
#     "state": "DRAFT",
#     "schema_version": 2,
#     "default_actions": [
#         "*"
#     ],
#     "definitions": [
#         "a definition"
#     ],
#     "sections": [
#         {
#             "key": "all_features_test",
#             "label": "All features test",
#             "lines": [
#                 {
#                     "key": "customer",
#                     "label": "Customer",
#                     "line_type": "text",
#                     "actions_on": [
#                         "camera",
#                         "gallery"
#                     ],
#                     "actions_off": [
#                         "notes"
#                     ],
#                     "description": "Do something here."
#                 },
#                 {
#                     "key": "location",
#                     "label": "Location",
#                     "line_type": "text",
#                     "actions_on": [],
#                     "actions_off": [],
#                     "description": None
#                 },
#                 {
#                     "key": "turbine",
#                     "label": "Turbine",
#                     "line_type": "text",
#                     "actions_on": [],
#                     "actions_off": [],
#                     "description": None
#                 },
#                 {
#                     "key": "equipment_oem",
#                     "label": "Equipment OEM",
#                     "line_type": "text",
#                     "actions_on": [
#                         "camera",
#                         "gallery"
#                     ],
#                     "actions_off": [],
#                     "description": None
#                 },
#                 {
#                     "key": "d_ring_rigging_eye",
#                     "label": "D-Ring Rigging Eye",
#                     "choices": [
#                         {
#                             "label": "",
#                             "value": ""
#                         },
#                         {
#                             "label": "Pass",
#                             "value": "Pass"
#                         },
#                         {
#                             "label": "Fail",
#                             "value": "Fail"
#                         },
#                         {
#                             "label": "N/A",
#                             "value": "N/A"
#                         }
#                     ],
#                     "line_type": "choice",
#                     "actions_on": [],
#                     "actions_off": [
#                         "notes"
#                     ],
#                     "description": "**Special Instructions** Inspect the 1.25 D-ring Rigging eye2. "
#                 },
#                 {
#                     "key": "broken_items",
#                     "label": "Broken Items",
#                     "choices": [
#                         {
#                             "label": "Thing 1",
#                             "value": "Thing 1"
#                         },
#                         {
#                             "label": "Thing 3",
#                             "value": "Thing 3"
#                         },
#                         {
#                             "label": "Thing 3",
#                             "value": "Thing 3"
#                         }
#                     ],
#                     "line_type": "multiple choice",
#                     "actions_on": [],
#                     "actions_off": [],
#                     "description": None
#                 },
#                 {
#                     "key": "image",
#                     "label": "Image",
#                     "line_type": "image",
#                     "actions_on": [],
#                     "actions_off": [],
#                     "description": None
#                 },
#                 {
#                     "key": "date_ended",
#                     "label": "Date Ended",
#                     "line_type": "date",
#                     "actions_on": [],
#                     "actions_off": [],
#                     "description": "**Instructions** Enter the date in the following format (mm/dd/yyyy) "
#                 },
#                 {
#                     "key": "this_is_a_really_long_string_of_text_we_want_to_put_into_this_report_n_n_its_really_great_to_be_working_on_this_project_loads_of_fun_is_being_had_by_all",
#                     "label": "This is a really long string of text we want to put into this report.\\n\\n Its really great to be working on this project. **Loads of fun** is being had by all",
#                     "line_type": "text block",
#                     "actions_on": [],
#                     "actions_off": [],
#                     "description": None
#                 },
#                 {
#                     "key": "sign_here",
#                     "label": "Sign Here",
#                     "line_type": "signature",
#                     "actions_on": [],
#                     "actions_off": [],
#                     "description": None
#                 },
#                 {
#                     "key": "select_vehicle_type",
#                     "label": "Select Vehicle Type",
#                     "choices": [
#                         {
#                             "label": "Chevorlet",
#                             "value": "Chevorlet"
#                         },
#                         {
#                             "label": "Ford",
#                             "value": "Ford"
#                         },
#                         {
#                             "label": "Tesla",
#                             "value": "Tesla"
#                         }
#                     ],
#                     "line_type": "choice",
#                     "actions_on": [],
#                     "actions_off": [],
#                     "description": None
#                 }
#             ],
#             "description": "This is a long text. "
#         },
#         {
#             "key": "another_section",
#             "label": "Another Section",
#             "lines": [
#                 {
#                     "key": "alfa",
#                     "label": "Alfa",
#                     "line_type": "text",
#                     "actions_on": [
#                         "camera",
#                         "gallery"
#                     ],
#                     "actions_off": [
#                         "notes"
#                     ],
#                     "description": "Do something here."
#                 },
#                 {
#                     "key": "bravo",
#                     "label": "Bravo",
#                     "line_type": "text",
#                     "actions_on": [],
#                     "actions_off": [],
#                     "description": None
#                 },
#                 {
#                     "key": "charlie",
#                     "label": "Charlie",
#                     "line_type": "text",
#                     "actions_on": [],
#                     "actions_off": [],
#                     "description": None
#                 },
#                 {
#                     "key": "delta",
#                     "label": "Delta",
#                     "line_type": "text",
#                     "actions_on": [
#                         "camera",
#                         "gallery"
#                     ],
#                     "actions_off": [],
#                     "description": None
#                 },
#                 {
#                     "key": "eco",
#                     "label": "Eco",
#                     "choices": [
#                         {
#                             "label": "",
#                             "value": ""
#                         },
#                         {
#                             "label": "Pass",
#                             "value": "Pass"
#                         },
#                         {
#                             "label": "Fail",
#                             "value": "Fail"
#                         },
#                         {
#                             "label": "N/A",
#                             "value": "N/A"
#                         }
#                     ],
#                     "line_type": "choice",
#                     "actions_on": [],
#                     "actions_off": [
#                         "notes"
#                     ],
#                     "description": "**Special Instructions** Inspect the 1.25 D-ring Rigging eye2. "
#                 },
#                 {
#                     "key": "abc",
#                     "label": "ABC",
#                     "choices": [
#                         {
#                             "label": "A1",
#                             "value": "A1"
#                         },
#                         {
#                             "label": "B1",
#                             "value": "B1"
#                         }
#                     ],
#                     "line_type": "multiple choice",
#                     "actions_on": [],
#                     "actions_off": [],
#                     "description": None
#                 },
#                 {
#                     "key": "image",
#                     "label": "Image",
#                     "line_type": "image",
#                     "actions_on": [],
#                     "actions_off": [],
#                     "description": None
#                 },
#                 {
#                     "key": "date_ended",
#                     "label": "Date Ended",
#                     "line_type": "date",
#                     "actions_on": [],
#                     "actions_off": [],
#                     "description": "**Instructions** Enter the date in the following format (mm/dd/yyyy) "
#                 },
#                 {
#                     "key": "this_is_a_really_long_string_of_text_we_want_to_put_into_this_report_n_n_its_really_great_to_be_working_on_this_project_loads_of_fun_is_being_had_by_all",
#                     "label": "This is a really long string of text we want to put into this report.\\n\\n Its really great to be working on this project. **Loads of fun** is being had by all",
#                     "line_type": "text block",
#                     "actions_on": [],
#                     "actions_off": [],
#                     "description": None
#                 },
#                 {
#                     "key": "sign_here",
#                     "label": "Sign Here",
#                     "line_type": "signature",
#                     "actions_on": [],
#                     "actions_off": [],
#                     "description": None
#                 },
#                 {
#                     "key": "select_vehicle_type",
#                     "label": "Select Vehicle Type",
#                     "choices": [
#                         {
#                             "label": "Chevorlet",
#                             "value": "Chevorlet"
#                         },
#                         {
#                             "label": "Ford",
#                             "value": "Ford"
#                         },
#                         {
#                             "label": "Tesla",
#                             "value": "Tesla"
#                         }
#                     ],
#                     "line_type": "choice",
#                     "actions_on": [],
#                     "actions_off": [],
#                     "description": None
#                 }
#             ],
#             "description": "This is a long text. "
#         }
#     ]
# }

# lineCount = 0
# resultCount = 0
# noteCount = 0
# mediaCount = 0

# for section in template["sections"]:
#     for line in section["lines"]:
#         lineCount += 1

# for section in payload:
#     for line in payload[section].values():
#         try:
#             if line["value"]:
#                 resultCount += 1
#         except KeyError:
#             continue
#         try:
#             if line["notes"]:
#                 noteCount += 1
#         except KeyError:
#             continue
#         try:
#             if line["media"]:
#                 mediaCount += 1
#         except KeyError:
#             continue

# print(f"lineCount: {lineCount}")
# print(f"resultCount: {resultCount}")
# print(round(float(resultCount) / float(lineCount), 4))
# print(f"noteCount: {noteCount}")
# print(f"mediaCount: {mediaCount}")

section = {
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
}

n_lines = 0
for item in section["lines"]:
    n_lines += 1

arr = ["desc", "type", "schema", "line"]

n_items = 0

for item in arr:
    print(item)
