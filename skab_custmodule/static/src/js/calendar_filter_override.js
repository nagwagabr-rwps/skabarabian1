/** @odoo-module **/

import CalendarModel from 'calendar.CalendarModel';

// Override the makeFilterAll method to restrict "Everybody's calendars" to specific group
CalendarModel.include({
    makeFilterAll(previousAllFilter, isUserOrPartner, sectionLabel) {
        // Check if the user belongs to a specific group (e.g., "Owner" group)
        const userHasAccess = this.env.session.user_has_group('skab_custmodule.group_calendar_owner');
        
        // If the user is not part of the group, do not show the filter
        if (!userHasAccess) {
            return null; // This disables the filter for unauthorized users
        }

        // Otherwise, return the original filter definition
        return this._super.apply(this, arguments);
    },
});