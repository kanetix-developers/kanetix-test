'use strict';

$(function(){

	$.get('/api/rates', function(rates) {

		for (var index in rates) {

			var id = rates[index][0];
			var rate = rates[index][1];

			(function(id, rate){
				$.get('/api/company/' + id, function(company_details) {
					$('#rates').append('<div>')
					$('#rates').append('<strong>' + rate + '</strong> ');
					$('#rates').append(company_details.name + ' (' + company_details.phone + ')');
					$('#rates').append('</div>');
				});
			})(id, rate);

		}

	});

});
