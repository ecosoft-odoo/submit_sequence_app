from . import __version__ as app_version

app_name = "submit_sequence_app"
app_title = "Submit Sequence App"
app_publisher = "Ecosoft"
app_description = "Run Sequence On Submit"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "kittiu@ecosoft.co.th"
app_license = "MIT"

fixtures = [
	{
		"dt": "Property Setter",
		"filters": [["name", "in", [
			"Sales Order-main-autoname",
		]]],
	},
]

doctype_js = {
	"Sales Order" : "public/js/sales_order.js",
}


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

