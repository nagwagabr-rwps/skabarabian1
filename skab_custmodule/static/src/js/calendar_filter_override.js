/** @odoo-module **/

import CalendarModel from 'calendar.CalendarModel';

// Override the makeFilterAll method to restrict "Everybody's calendars" to managers
CalendarModel.include({
    makeFilterAll(previousAllFilter, isUserOrPartner, sectionLabel) {
        // Check if the user belongs to the manager group
        const userHasAccess = this.env.session.user_has_group('appointment.group_appointment_manager');
        
        // If the user is not part of the manager group, do not show the filter
        if (!userHasAccess) {
            return null; // This disables the filter for unauthorized users
        }

        // Otherwise, return the original filter definition
        return this._super.apply(this, arguments);
    },
});
