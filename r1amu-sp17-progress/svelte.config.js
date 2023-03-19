//import adapter from '@sveltejs/adapter-auto';
import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/kit/vite';
import { dirname, join } from "path";
import { cssModules } from 'svelte-preprocess-cssmodules';
import { fileURLToPath } from 'url';

/** @type {import('@sveltejs/kit').Config} */
export const config = {
	kit: {
		// adapter: adapter()
		adapter: adapter({
			pages: "build", assets: "build", fallback: null, precompress: false
		}),
		paths: { base: process.env.NODE_ENV === "production" ? "/ddr-result/r1amu-sp17-progress" : "" }
	},
	preprocess: [
		vitePreprocess({
			style: {
				css: {
					postcss: join(
						dirname(fileURLToPath(import.meta.url)),
						"postcss.config.cjs")
				}
			}
		}),
		cssModules(),
	]
};

export default config;