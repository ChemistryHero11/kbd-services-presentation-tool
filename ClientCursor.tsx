import * as React from 'react';
import { Box } from '@mui/material';
import MousePointerIcon from '@mui/icons-material/Mouse';
import { useSelector } from 'react-redux';
import { RootState } from '../store/store';
import { CursorPosition } from '../types';

interface ClientCursorProps {
  cursorPosition: CursorPosition;
  showCursor?: boolean;
}

/**
 * Component that displays a cursor that can be controlled remotely
 * during a live presentation session
 */
const ClientCursor: React.FC<ClientCursorProps> = ({ cursorPosition, showCursor = true }) => {
  if (!showCursor) return null;

  return (
    <Box
      sx={{
        position: 'fixed',
        left: `${cursorPosition.x}%`,
        top: `${cursorPosition.y}%`,
        zIndex: 9999,
        pointerEvents: 'none',
        transform: 'translate(-50%, -50%)',
        transition: 'all 0.1s ease-out',
      }}
    >
      <MousePointerIcon
        sx={{
          color: 'primary.main',
          fontSize: '2rem',
          filter: 'drop-shadow(0px 0px 2px rgba(0,0,0,0.5))',
        }}
      />
    </Box>
  );
};

// Wrapper component that connects to Redux store
interface ConnectedClientCursorProps {}

export const ConnectedClientCursor: React.FC<ConnectedClientCursorProps> = () => {
  const { cursorPosition, showCursor } = useSelector((state: RootState) => ({
    cursorPosition: state.presentation.cursorPosition,
    showCursor: state.presentation.showCursor
  }));
  
  return <ClientCursor cursorPosition={cursorPosition} showCursor={showCursor} />;
};

export default ClientCursor;
