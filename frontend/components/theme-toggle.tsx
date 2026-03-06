'use client';

import { Moon, Sun } from 'lucide-react';
import { useTheme } from 'next-themes';

export function ThemeToggle() {
  const { theme, setTheme } = useTheme();
  return (
    <button
      className='inline-flex h-9 w-9 items-center justify-center rounded-md border border-border bg-background'
      onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
      aria-label='Toggle theme'
    >
      <Sun className='h-4 w-4 dark:hidden' />
      <Moon className='hidden h-4 w-4 dark:block' />
    </button>
  );
}
