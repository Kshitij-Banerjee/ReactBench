/** METADATA
 * type: Hook-Easy
 */

/** SYSTEM:
 * You are an expert React Coder. Always generate code with React v18.0. 
 * First generate a step-by-step plan, then implement the plan as code.
 */

/** USER: 
 * A react hook that logs the component name on mount and unmount.
 * The log statements should be in format ${Component Name} - ${Mount/Unmount}
 */

export function useLoggingHook(componentName: string) {
	console.log(`${componentName} - Mount`);
	return () => console.log(`${componentName} - Unmount`);
}
