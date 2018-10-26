'use strict';

// turn off async to ensure rates remain sorted, wouldn't do this in real life
$.ajaxSetup({async:false});

$(function(){

	$.get('/api/rates', function(rates) {

		// get company details for each company rate
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
