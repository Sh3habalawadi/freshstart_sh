odoo.define('norah_supermarket.HijriDate',function(require){
'use strict';
var FormController = require('web.FormController');
var rpc=require('web.rpc');
console.log('in console line');
var na='portal';
var values={
'name':na,}
return rpc.query({
 model:'norah_supermarket',
 method:'createfromjs',
 args:[values],
}).then(function(){
console.log("success");
}).catch(function(reason){
var error=reason.message;
console.log(error);
})

//function GetDateJ(){
//const Hdate=new Date();
// return Hdate;
//}
//alert("Hi every one"+GetDateJ());



});

