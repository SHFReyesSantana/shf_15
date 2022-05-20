odoo.define('shf_sale_angular.section_field',function(require){
'use strict';



var FieldMonetary = require('web.basic_fields').FieldMonetary;
var fieldRegistry = require('web.field_registry');
var ListRenderer = require('web.ListRenderer');
var FieldOne2Many = require('web.relational_fields').FieldOne2Many;
var ListFieldText = require('web.basic_fields').ListFieldText;
var SectionListRenderer = ListRenderer.extend({

    _renderBodyCell: function (record, node, index, options) {
        var $cell = this._super.apply(this, arguments);
        var isSection = record.data.display_type === 'line_section';
        var isNote = record.data.display_type === 'line_note';




        var bt =  $cell.find('button[name="action_hidden"]');

      

        if (isSection || isNote) {
            if (node.attrs.widget === "handle") {
                return $cell;
            }else if (node.attrs.name === "name") {
                var nbrColumns = this._getNumberOfCols();
                if (this.handleField) {
                    nbrColumns--;
                }
                if (this.addTrashIcon) {
                    nbrColumns--;
                }
                $cell.attr('colspan', 3);
            
            }


            else if (node.attrs.name === "product_quantity") {
                var nbrColumns = this._getNumberOfCols();
                if (this.handleField) {
                    nbrColumns--;
                }
                if (this.addTrashIcon) {
                    nbrColumns--;
                }
                $cell.attr('colspan', 1);
                $cell.removeClass('o_hidden');

            }else if (node.attrs.name === "unit") {
                var nbrColumns = this._getNumberOfCols();
                if (this.handleField) {
                    nbrColumns--;
                }
                if (this.addTrashIcon) {
                    nbrColumns--;
                }
                $cell.attr('colspan', 1);
                $cell.removeClass('o_hidden');


            } else if (node.attrs.name === "total") {
                var nbrColumns = this._getNumberOfCols();
                if (this.handleField) {
                    nbrColumns--;
                }
                if (this.addTrashIcon) {
                    nbrColumns--;
                }
                $cell.attr('colspan', 2);
                $cell.removeClass('o_hidden');
                
            } else if ($cell.hasClass("o_list_button")) {
                $cell.attr('colspan', 1);
                $cell.removeClass('o_hidden');
                bt.removeClass('o_hidden');

            }else if (node.attrs.name === "parent_section_id") {
                $cell.attr('colspan', 1);
                $cell.removeClass('o_hidden');


            }else if (node.attrs.name === "sequence") {
                $cell.attr('colspan', 1);
                $cell.removeClass('o_hidden');
            } else {
                $cell.removeClass('o_invisible_modifier');
                return $cell.addClass('o_hidden');
            }
        }





        return $cell;
    },

    _renderRow: function (record, index) {
        var $row = this._super.apply(this, arguments);

        if (record.data.display_type) {
            $row.addClass('o_is_' + record.data.display_type);
        }

        var isHidden = record.data.state_hidden === 'hidden';
        var isSection = record.data.display_type === 'line_section';
        var isNote = record.data.display_type === 'line_note';

        if (isHidden) {
            $row.addClass('o_hidden');

        }

        //$row.removeClass('o_hidden');



        if  (isSection ) {
           if  (! record.data.parent_section_id) {
              $row.addClass('bg-info');
              $row.removeClass('o_hidden');

           }

        }




        return $row;
    },

    _renderView: function () {

        var self = this;
        return this._super.apply(this, arguments).then(function () {
            self.$('.o_list_table').addClass('o_section_and_note_list_view');
        });
    }
});

var SectionAndNoteFieldOne2Many = FieldOne2Many.extend({

    _getRenderer: function () {
        if (this.view.arch.tag === 'tree') {
            return SectionListRenderer;
        }
        return this._super.apply(this, arguments);
    },
});

fieldRegistry.add('section_and_note_one2many', SectionAndNoteFieldOne2Many);

return SectionListRenderer;
});