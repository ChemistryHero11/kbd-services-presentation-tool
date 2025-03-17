import * as React from 'react';
import { useDispatch } from 'react-redux';
import { Box, Typography, Paper } from '@mui/material';
import { setClientInfo } from '../store/presentationSlice';
import { ClientInfo } from '../types';
import { ConnectedClientCursor } from './ClientCursor';

const ClientView: React.FC = () => {
  const dispatch = useDispatch();
  
  // Sample client info for testing that matches the ClientInfo interface
  const clientInfo: ClientInfo = {
    companyName: 'Acme Corporation',
    contactName: 'John Doe',
    position: 'Marketing Director',
    email: 'john@acme.com',
    phone: '555-123-4567',
    address: '123 Main St, Anytown, USA',
    industry: 'Retail',
    size: 'Medium',
    previousClient: true,
    preferences: {
      productTypes: ['Apparel', 'Writing Instruments'],
      budget: 'Medium',
      timeline: '4 weeks',
      quantity: '500-1000',
      brandColors: ['#1976d2', '#dc004e'],
      additionalNotes: 'Looking for eco-friendly options'
    },
    notes: 'Previous client with good payment history',
    interests: ['Promotional events', 'Employee gifts']
  };
  
  React.useEffect(() => {
    // Set client info in Redux store
    dispatch(setClientInfo(clientInfo));
  }, [dispatch]);
  
  return (
    <Box sx={{ p: 3 }}>
      <Paper elevation={3} sx={{ p: 3, mb: 3 }}>
        <Typography variant="h4" gutterBottom>
          Client: {clientInfo.companyName}
        </Typography>
        <Typography variant="body1">
          Contact: {clientInfo.contactName}
        </Typography>
        <Typography variant="body1">
          Industry: {clientInfo.industry}
        </Typography>
        <Typography variant="body1">
          Previous Client: {clientInfo.previousClient ? 'Yes' : 'No'}
        </Typography>
      </Paper>
      
      {/* Cursor will be shown based on Redux state */}
      <ConnectedClientCursor />
    </Box>
  );
};

export default ClientView;
