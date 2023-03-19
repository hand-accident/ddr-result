import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';
import tailwindcss from "tailwindcss";
import autoprefixer from 'autoprefixer';
import postcssNesting from "postcss-nesting";
import path from 'path';
import { cssModules } from 'svelte-preprocess-cssmodules';

export default defineConfig({
	css: {
		postcss: {
			plugins: [
				tailwindcss(),
				autoprefixer(),
				postcssNesting()]
		},
		modules: {}
	},
	plugins: [sveltekit()],
	define: { 'process.env': process.env },
	resolve: {
		alias: {
			$lib: path.resolve("./src/lib"),
			$l: path.resolve("./src/lib/layout"),
			$a: path.resolve("./src/lib/arith"),
			$c: path.resolve("./src/lib/cell"),
			$g: path.resolve("./src/lib/group"),
			$w: path.resolve("./src/lib/world"),
		}
	}
});