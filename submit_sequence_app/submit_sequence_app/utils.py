import frappe


@frappe.whitelist()
def rename_sales_order(doctype, naming_series, docname):
    new_name = frappe.model.naming.make_autoname(naming_series, doctype)
    docname = frappe.model.rename_doc.rename_doc(doctype=doctype, old=docname, new=new_name)
    return docname