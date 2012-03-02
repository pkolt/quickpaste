tinyMCEPopup.requireLangPack();

var QuickPasteDialog = {
	insert : function(link) {
		tinyMCEPopup.editor.execCommand('mceInsertContent', false, link);
		tinyMCEPopup.close();
	}
};

tinyMCEPopup.onInit.add(QuickPasteDialog.init, QuickPasteDialog);