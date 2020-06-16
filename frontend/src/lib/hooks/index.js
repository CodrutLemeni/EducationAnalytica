import { useCallback, useState } from 'react';

export function useModal() {
  const [ isOpen, setIsOpen ] = useState(false);
  const [ data, setData ] = useState(null);
  const open = useCallback((data) => {
    setIsOpen(true);
    setData(data);
  }, []);

  const close = useCallback(() => {
    setIsOpen(false);
    // setData({});
  }, []);

  return { isOpen, open, close, data };
}
