import streamlit as st
import pandas as pd
import numpy as np


# Sample data
def load_sample_data():
    # Replace with actual data loading logic
    donors = pd.DataFrame({
        'Name': ['John Doe', 'Jane Smith'],
        'Amount Donated': [500, 300],
        'Date': ['2024-01-15', '2024-02-20']
    })
    volunteers = pd.DataFrame({
        'Name': ['Alice Johnson', 'Bob Brown'],
        'Hours Volunteered': [10, 8],
        'Role': ['Coordinator', 'Volunteer']
    })
    events = pd.DataFrame({
        'Event Name': ['Gala', 'Fundraiser'],
        'Date': ['2024-03-10', '2024-04-05'],
        'Attendees': [150, 200]
    })
    expenses = pd.DataFrame({
        'Expense Name': ['Office Supplies', 'Event Catering'],
        'Amount': [200, 500],
        'Date': ['2024-01-20', '2024-03-15']
    })
    return donors, volunteers, events, expenses

def main():
    st.title("Father First Non-Profit Systems")

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Select a page", [
        "Dashboard", 
        "Donor Management", 
        "Volunteer Management", 
        "Event Management", 
        "Financial Management", 
        "Reporting and Analytics", 
        "Communication Hub", 
        "Settings and Administration"
    ])

    donors, volunteers, events, expenses = load_sample_data()

    if page == "Dashboard":
    st.header("Dashboard")
    st.write("Welcome to the Dashboard! Here, you can explore an overview of key metrics that highlight the impact of our organization. Track donations, volunteer efforts, and stay informed about upcoming events.")

    # Donation Overview
    st.subheader("Donation Overview")
    st.write("This chart provides an overview of the donations received over time, helping us understand donation patterns and trends.")
    donation_data = donors.groupby('Date')['Amount Donated'].sum()
    st.line_chart(donation_data)

    # Insightful stats
    st.write(f"As of today, we have received a total of **${donation_data.sum():,.2f}** in donations.")

    # Volunteer Hours
    st.subheader("Volunteer Hours Distribution")
    st.write("Here, we present a breakdown of the total hours volunteered, categorized by the roles our volunteers have undertaken.")
    volunteer_data = volunteers.groupby('Role')['Hours Volunteered'].sum()
    st.bar_chart(volunteer_data)
    
    # Highlight key contributions
    st.write("Our volunteers have collectively contributed **{volunteer_data.sum()}** hours of service. The chart above showcases the distribution of these hours across various roles.")

    # Upcoming Events
    st.subheader("Upcoming Events")
    st.write("Stay informed about our upcoming events. Your participation can make a difference!")
    st.table(events)

    # Recent Activities
    st.subheader("Recent Activities")
    st.write("A glance at the most recent activities, including donations and volunteer contributions. These activities reflect the ongoing support from our community.")
    recent_activities = pd.concat([donors, volunteers], keys=['Donors', 'Volunteers'])
    st.write(recent_activities.sort_values(by='Date', ascending=False).head(10))

    # Total Donations and Volunteer Hours
    st.subheader("Impact Summary")
    st.write("The figures below summarize the total impact of our collective efforts.")
    total_donations = donors['Amount Donated'].sum()
    total_volunteer_hours = volunteers['Hours Volunteered'].sum()
    st.metric(label="Total Donations", value=f"${total_donations:,.2f}")
    st.metric(label="Total Volunteer Hours", value=f"{total_volunteer_hours} hours")

    # Additional Features and Insights
    st.subheader("Donation Trends by Donor Type")
    st.write("Explore how donations vary across different types of donors.")
    donation_trends = donors.groupby(['Donor Type', 'Date'])['Amount Donated'].sum().unstack().fillna(0)
    st.area_chart(donation_trends)

    st.subheader("Volunteer Engagement Over Time")
    st.write("Analyze the engagement of volunteers over time, helping us identify peak periods of activity.")
    volunteer_engagement = volunteers.groupby('Date')['Hours Volunteered'].sum()
    st.line_chart(volunteer_engagement)

    st.subheader("Donor and Volunteer Breakdown")
    st.write("The following charts provide a detailed breakdown of donors and volunteers by various categories.")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Donors by Type**")
        donor_type_data = donors['Donor Type'].value_counts()
        st.bar_chart(donor_type_data)
    
    with col2:
        st.write("**Volunteers by Role**")
        volunteer_role_data = volunteers['Role'].value_counts()
        st.bar_chart(volunteer_role_data)
    
    # Call to action
    st.subheader("Get Involved")
    st.write("Your continued support is vital. Whether through donations or volunteer work, there are many ways to contribute.")
    st.button("Donate Now")
    st.button("Sign Up as a Volunteer")

    elif page == "Donor Management":
        st.header("Donor Management")
        
        # View and manage donor information
        st.subheader("View Donors")
        st.write(donors)
        
        # Add donor
        st.subheader("Add New Donor")
        with st.form("add_donor_form"):
            name = st.text_input("Donor Name")
            amount = st.number_input("Amount Donated", min_value=0.0)
            date = st.date_input("Donation Date")
            submit_button = st.form_submit_button("Add Donor")
            if submit_button:
                new_donor = pd.DataFrame({
                    'Name': [name],
                    'Amount Donated': [amount],
                    'Date': [date]
                })
                donors = donors.append(new_donor, ignore_index=True)
                st.success("Donor added successfully!")
                st.write(donors)

        # Update donor
        st.subheader("Update Donor Information")
        donor_name = st.selectbox("Select Donor to Update", donors['Name'].unique())
        updated_amount = st.number_input("Update Amount Donated", min_value=0.0)
        if st.button("Update Donor"):
            donors.loc[donors['Name'] == donor_name, 'Amount Donated'] = updated_amount
            st.success("Donor updated successfully!")
            st.write(donors)

        # Delete donor
        st.subheader("Delete Donor")
        delete_name = st.selectbox("Select Donor to Delete", donors['Name'].unique())
        if st.button("Delete Donor"):
            donors = donors[donors['Name'] != delete_name]
            st.success("Donor deleted successfully!")
            st.write(donors)

    elif page == "Volunteer Management":
        st.header("Volunteer Management")
        
        # Manage volunteer information
        st.subheader("View Volunteers")
        st.write(volunteers)
        
        # Add volunteer
        st.subheader("Add New Volunteer")
        with st.form("add_volunteer_form"):
            name = st.text_input("Volunteer Name")
            hours = st.number_input("Hours Volunteered", min_value=0)
            role = st.text_input("Role")
            submit_button = st.form_submit_button("Add Volunteer")
            if submit_button:
                new_volunteer = pd.DataFrame({
                    'Name': [name],
                    'Hours Volunteered': [hours],
                    'Role': [role]
                })
                volunteers = volunteers.append(new_volunteer, ignore_index=True)
                st.success("Volunteer added successfully!")
                st.write(volunteers)

        # Update volunteer
        st.subheader("Update Volunteer Information")
        volunteer_name = st.selectbox("Select Volunteer to Update", volunteers['Name'].unique())
        updated_hours = st.number_input("Update Hours Volunteered", min_value=0)
        if st.button("Update Volunteer"):
            volunteers.loc[volunteers['Name'] == volunteer_name, 'Hours Volunteered'] = updated_hours
            st.success("Volunteer updated successfully!")
            st.write(volunteers)

        # Delete volunteer
        st.subheader("Delete Volunteer")
        delete_name = st.selectbox("Select Volunteer to Delete", volunteers['Name'].unique())
        if st.button("Delete Volunteer"):
            volunteers = volunteers[volunteers['Name'] != delete_name]
            st.success("Volunteer deleted successfully!")
            st.write(volunteers)

    elif page == "Event Management":
        st.header("Event Management")
        
        # View and manage events
        st.subheader("View Events")
        st.write(events)
        
        # Add event
        st.subheader("Add New Event")
        with st.form("add_event_form"):
            event_name = st.text_input("Event Name")
            event_date = st.date_input("Event Date")
            attendees = st.number_input("Number of Attendees", min_value=0)
            submit_button = st.form_submit_button("Add Event")
            if submit_button:
                new_event = pd.DataFrame({
                    'Event Name': [event_name],
                    'Date': [event_date],
                    'Attendees': [attendees]
                })
                events = events.append(new_event, ignore_index=True)
                st.success("Event added successfully!")
                st.write(events)

        # Update event
        st.subheader("Update Event Information")
        event_to_update = st.selectbox("Select Event to Update", events['Event Name'].unique())
        updated_attendees = st.number_input("Update Number of Attendees", min_value=0)
        if st.button("Update Event"):
            events.loc[events['Event Name'] == event_to_update, 'Attendees'] = updated_attendees
            st.success("Event updated successfully!")
            st.write(events)

        # Delete event
        st.subheader("Delete Event")
        event_to_delete = st.selectbox("Select Event to Delete", events['Event Name'].unique())
        if st.button("Delete Event"):
            events = events[events['Event Name'] != event_to_delete]
            st.success("Event deleted successfully!")
            st.write(events)

    elif page == "Financial Management":
        st.header("Financial Management")
        
        # View and manage expenses
        st.subheader("View Expenses")
        st.write(expenses)
        
        # Add expense
        st.subheader("Add New Expense")
        with st.form("add_expense_form"):
            expense_name = st.text_input("Expense Name")
            expense_amount = st.number_input("Expense Amount", min_value=0.0)
            expense_date = st.date_input("Expense Date")
            submit_button = st.form_submit_button("Add Expense")
            if submit_button:
                new_expense = pd.DataFrame({
                    'Expense Name': [expense_name],
                    'Amount': [expense_amount],
                    'Date': [expense_date]
                })
                expenses = expenses.append(new_expense, ignore_index=True)
                st.success("Expense added successfully!")
                st.write(expenses)

        # Update expense
        st.subheader("Update Expense Information")
        expense_to_update = st.selectbox("Select Expense to Update", expenses['Expense Name'].unique())
        updated_amount = st.number_input("Update Expense Amount", min_value=0.0)
        if st.button("Update Expense"):
            expenses.loc[expenses['Expense Name'] == expense_to_update, 'Amount'] = updated_amount
            st.success("Expense updated successfully!")
            st.write(expenses)

        # Delete expense
        st.subheader("Delete Expense")
        expense_to_delete = st.selectbox("Select Expense to Delete", expenses['Expense Name'].unique())
        if st.button("Delete Expense"):
            expenses = expenses[expenses['Expense Name'] != expense_to_delete]
            st.success("Expense deleted successfully!")
            st.write(expenses)

    elif page == "Reporting and Analytics":
        st.header("Reporting and Analytics")
        st.write("Generate detailed reports and customize analytics.")
        
        # Donation report
        st.subheader("Donation Report")
        donation_data = donors.groupby('Date')['Amount Donated'].sum()
        st.line_chart(donation_data)
        st.write("Detailed donation report.")
        
        # Volunteer report
        st.subheader("Volunteer Report")
        volunteer_data = volunteers.groupby('Role')['Hours Volunteered'].sum()
        st.bar_chart(volunteer_data)
        st.write("Detailed volunteer report.")
        
        # Event report
        st.subheader("Event Report")
        event_data = events.groupby('Date')['Attendees'].sum()
        st.line_chart(event_data)
        st.write("Detailed event report.")
        
        # Expense report
        st.subheader("Expense Report")
        expense_data = expenses.groupby('Date')['Amount'].sum()
        st.line_chart(expense_data)
        st.write("Detailed expense report.")
        
        # Customizable analytics
        st.subheader("Custom Analytics")
        category = st.selectbox("Select Category", ["Donations", "Volunteers", "Events", "Expenses"])
        if category == "Donations":
            st.line_chart(donation_data)
        elif category == "Volunteers":
            st.bar_chart(volunteer_data)
        elif category == "Events":
            st.line_chart(event_data)
        elif category == "Expenses":
            st.line_chart(expense_data)

    elif page == "Communication Hub":
        st.header("Communication Hub")
        st.write("Send updates and communications to donors, volunteers, and stakeholders.")
        
        # Send email or SMS
        st.subheader("Send Communication")
        recipient = st.selectbox("Select Recipient", ["Donors", "Volunteers", "All"])
        message = st.text_area("Message")
        communication_type = st.selectbox("Select Communication Type", ["Email", "SMS"])
        if st.button("Send Message"):
            st.success(f"Message sent to {recipient} via {communication_type}!")
            # Integrate email/SMS functionality here

        # Communication history
        st.subheader("Communication History")
        # Add functionality to view past communications

    elif page == "Settings and Administration":
        st.header("Settings and Administration")
        st.write("Manage system settings, user roles, and permissions.")
        
        # Manage users
        st.subheader("Manage Users")
        with st.form("manage_users_form"):
            user_name = st.text_input("User Name")
            user_role = st.selectbox("User Role", ["Admin", "Manager", "User"])
            submit_button = st.form_submit_button("Add User")
            if submit_button:
                st.success(f"User {user_name} added with role {user_role}!")
                # Add actual user management functionality

        # System settings
        st.subheader("System Settings")
        setting = st.selectbox("Select Setting", ["General", "Security", "Notifications"])
        if setting == "General":
            st.write("General settings management.")
        elif setting == "Security":
            st.write("Security settings management.")
        elif setting == "Notifications":
            st.write("Notification settings management.")
        
        # Backup and restore
        st.subheader("Backup and Restore")
        if st.button("Backup Data"):
            st.success("Data backed up successfully!")
            # Integrate backup functionality
        if st.button("Restore Data"):
            st.success("Data restored successfully!")
            # Integrate restore functionality

if __name__ == "__main__":
    main()
