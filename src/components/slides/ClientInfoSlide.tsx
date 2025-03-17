import * as React from 'react';
import { useSelector } from 'react-redux';
import { Box, Typography, Paper, Grid, Avatar } from '@mui/material';
import { RootState } from '../../store/store';

const ClientInfoSlide: React.FC = () => {
  const clientInfo = useSelector((state: RootState) => state.presentation.clientInfo);

  if (!clientInfo) {
    return (
      <Box sx={{ p: 4, textAlign: 'center' }}>
        <Typography variant="h5">No client information available</Typography>
      </Box>
    );
  }

  return (
    <Box sx={{ p: 4 }}>
      <Paper elevation={3} sx={{ p: 4, borderRadius: 2 }}>
        <Grid container spacing={4}>
          <Grid item xs={12} md={4} sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            {clientInfo.logo ? (
              <Avatar 
                src={clientInfo.logo} 
                alt={clientInfo.companyName}
                sx={{ width: 150, height: 150, mb: 2 }}
              />
            ) : (
              <Avatar 
                sx={{ width: 150, height: 150, mb: 2, bgcolor: 'primary.main' }}
              >
                {clientInfo.companyName?.charAt(0) || 'C'}
              </Avatar>
            )}
            <Typography variant="h4" gutterBottom>
              {clientInfo.companyName}
            </Typography>
            <Typography variant="subtitle1" color="text.secondary">
              {clientInfo.industry}
            </Typography>
          </Grid>
          
          <Grid item xs={12} md={8}>
            <Typography variant="h5" gutterBottom sx={{ borderBottom: '1px solid', borderColor: 'divider', pb: 1 }}>
              Client Details
            </Typography>
            
            <Grid container spacing={2}>
              <Grid item xs={12} sm={6}>
                <Typography variant="subtitle2" color="text.secondary">Contact Person</Typography>
                <Typography variant="body1" gutterBottom>{clientInfo.contactName}</Typography>
                
                {clientInfo.position && (
                  <>
                    <Typography variant="subtitle2" color="text.secondary">Position</Typography>
                    <Typography variant="body1" gutterBottom>{clientInfo.position}</Typography>
                  </>
                )}
                
                {clientInfo.email && (
                  <>
                    <Typography variant="subtitle2" color="text.secondary">Email</Typography>
                    <Typography variant="body1" gutterBottom>{clientInfo.email}</Typography>
                  </>
                )}
                
                {clientInfo.phone && (
                  <>
                    <Typography variant="subtitle2" color="text.secondary">Phone</Typography>
                    <Typography variant="body1" gutterBottom>{clientInfo.phone}</Typography>
                  </>
                )}
              </Grid>
              
              <Grid item xs={12} sm={6}>
                {clientInfo.address && (
                  <>
                    <Typography variant="subtitle2" color="text.secondary">Address</Typography>
                    <Typography variant="body1" gutterBottom>{clientInfo.address}</Typography>
                  </>
                )}
                
                {clientInfo.size && (
                  <>
                    <Typography variant="subtitle2" color="text.secondary">Company Size</Typography>
                    <Typography variant="body1" gutterBottom>{clientInfo.size}</Typography>
                  </>
                )}
                
                <Typography variant="subtitle2" color="text.secondary">Previous Client</Typography>
                <Typography variant="body1" gutterBottom>{clientInfo.previousClient ? 'Yes' : 'No'}</Typography>
              </Grid>
            </Grid>
            
            {clientInfo.preferences && (
              <Box sx={{ mt: 3 }}>
                <Typography variant="h5" gutterBottom sx={{ borderBottom: '1px solid', borderColor: 'divider', pb: 1 }}>
                  Preferences
                </Typography>
                
                <Grid container spacing={2}>
                  {clientInfo.preferences.productTypes && (
                    <Grid item xs={12} sm={6}>
                      <Typography variant="subtitle2" color="text.secondary">Product Types</Typography>
                      <Typography variant="body1" gutterBottom>
                        {clientInfo.preferences.productTypes.join(', ')}
                      </Typography>
                    </Grid>
                  )}
                  
                  {clientInfo.preferences.budget && (
                    <Grid item xs={12} sm={6}>
                      <Typography variant="subtitle2" color="text.secondary">Budget</Typography>
                      <Typography variant="body1" gutterBottom>{clientInfo.preferences.budget}</Typography>
                    </Grid>
                  )}
                  
                  {clientInfo.preferences.timeline && (
                    <Grid item xs={12} sm={6}>
                      <Typography variant="subtitle2" color="text.secondary">Timeline</Typography>
                      <Typography variant="body1" gutterBottom>{clientInfo.preferences.timeline}</Typography>
                    </Grid>
                  )}
                  
                  {clientInfo.preferences.quantity && (
                    <Grid item xs={12} sm={6}>
                      <Typography variant="subtitle2" color="text.secondary">Quantity</Typography>
                      <Typography variant="body1" gutterBottom>{clientInfo.preferences.quantity}</Typography>
                    </Grid>
                  )}
                </Grid>
              </Box>
            )}
            
            {clientInfo.notes && (
              <Box sx={{ mt: 3 }}>
                <Typography variant="subtitle2" color="text.secondary">Notes</Typography>
                <Typography variant="body1">{clientInfo.notes}</Typography>
              </Box>
            )}
          </Grid>
        </Grid>
      </Paper>
    </Box>
  );
};

export default ClientInfoSlide;
