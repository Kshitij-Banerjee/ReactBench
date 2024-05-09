import {renderHook} from '@testing-library/react'
import '@testing-library/jest-dom'
import { useLoggingHook } from './MountUnmountHook_Canonical';

describe('Eval_MountUnmountHOok', () => {
	test('logs to console the mount event', () => {
		const consoleSpy = jest.spyOn(console, 'log');
		renderHook(useLoggingHook('COMPONENT NAME'));
		expect(consoleSpy).toHaveBeenCalledWith('COMPONENT NAME - Mount')
	});

	test('logs to console on unmount event', () => {
		const consoleSpy = jest.spyOn(console, 'log');
		const { unmount } = renderHook(useLoggingHook('COMPONENT NAME'));
		unmount();
		expect(consoleSpy).toHaveBeenCalledWith('COMPONENT NAME - Unmount')
	});
})