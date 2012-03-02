(function() {
	tinymce.PluginManager.requireLangPack('quickpaste');
	tinymce.create('tinymce.plugins.QuickPastePlugin', {
		init : function(ed, url) {
			ed.addCommand('mceDownloader', function() {
				ed.windowManager.open({
					file : '/quickpaste/',
					width : 420 + parseInt(ed.getLang('quickpaste.delta_width', 0)),
					height : 140 + parseInt(ed.getLang('quickpaste.delta_height', 0)),
					inline : 1
				}, {
					plugin_url : url
				});
			});

			ed.addButton('quickpaste', {
				title : 'quickpaste.desc',
				cmd : 'mceDownloader',
				image : url + '/img/icon.gif'
			});

		},

		createControl : function(n, cm) {
			return null;
		},

		getInfo : function() {
			return {
				longname : 'Quickpaste plugin',
				author : 'Pavel Koltyshev',
				authorurl : 'http://github.com/pkolt/quickpaste',
				infourl : 'http://github.com/pkolt/quickpaste',
				version : "1.2.0"
			};
		}
	});

	tinymce.PluginManager.add('quickpaste', tinymce.plugins.QuickPastePlugin);
})();
