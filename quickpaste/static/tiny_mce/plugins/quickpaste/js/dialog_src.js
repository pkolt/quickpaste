tinyMCEPopup.requireLangPack();

var QuickPasteDialog = {
    init: function(ed){},
    insert : function(link) {
	tinyMCEPopup.editor.execCommand('mceInsertContent', false, link);
	tinyMCEPopup.close();
    }
};

tinyMCEPopup.onInit.add(QuickPasteDialog.init, QuickPasteDialog);