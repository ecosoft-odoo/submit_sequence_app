// Copyright (c) 2018, Frappe Technologies Pvt. Ltd. and Contributors
// MIT License. See license.txt


frappe.ui.form.on("Sales Order", {

	on_submit: function(frm) {

		const doctype = frm.doctype;
		const docname = frm.doc.name;
		const naming_series = frm.doc.naming_series;

		let rename_document = () => {
			return frappe.xcall("submit_sequence_app.submit_sequence_app.utils.rename_sales_order", {
				doctype: doctype,
				naming_series: naming_series,
				docname: docname
			}).then(new_docname => {
				if (new_docname != docname) {
					$(document).trigger("rename", [doctype, docname, new_docname]);
					if (locals[doctype] && locals[doctype][docname]) delete locals[doctype][docname];
				}
				frm.reload_doc();
			});
		};

		return new Promise((resolve, reject) => {
			rename_document().then(resolve).catch(reject);
		});
	},

});
