import * as React from 'react';
import { useSelector } from 'react-redux';
import { Box } from '@mui/material';
import { RootState } from '../store/store';
import ClientInfoSlide from './slides/ClientInfoSlide';

interface SlidesContainerProps {
  isPresenter?: boolean;
}

const SlidesContainer: React.FC<SlidesContainerProps> = ({ isPresenter = false }) => {
  const currentSlide = useSelector((state: RootState) => state.presentation.currentSlide);
  
  // Array of slide components
  const slides = [
    <ClientInfoSlide key="client-info" />
    // Add more slides here as they are created
  ];
  
  return (
    <Box
      sx={{
        width: '100%',
        height: '100%',
        overflow: 'hidden',
        position: 'relative',
        bgcolor: 'background.paper',
      }}
    >
      {slides[currentSlide] || slides[0]}
    </Box>
  );
};

export default SlidesContainer;
