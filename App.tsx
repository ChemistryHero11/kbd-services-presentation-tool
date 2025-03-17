import * as React from 'react';
import { Box, Container } from '@mui/material';
import ClientView from './components/ClientView';
import SlidesContainer from './components/SlidesContainer';
import { ConnectedClientCursor } from './components/ClientCursor';

const App: React.FC = () => {
  return (
    <Container maxWidth={false} disableGutters sx={{ height: '100vh', overflow: 'hidden' }}>
      <Box sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}>
        <ClientView />
        <Box sx={{ flexGrow: 1 }}>
          <SlidesContainer />
        </Box>
        <ConnectedClientCursor />
      </Box>
    </Container>
  );
};

export default App;
