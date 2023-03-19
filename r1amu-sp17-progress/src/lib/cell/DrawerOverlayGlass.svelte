<script>
    let className, labelFor;
    export { className as class, labelFor as for };
    export let checked;
</script>

<label for={labelFor} class="c gl {className}" class:checked>
    <slot />
</label>

<style lang="postcss" module>
    .c {
        /* drawer-overlay*/
        @apply cursor-pointer bg-neutral-focus transition-all duration-300 ease-in-out;
        @apply invisible col-start-1 row-start-1 opacity-0;
    }
    .checked {
        /* drawer-overlay (toggle checked)*/
        opacity: 0.999999; /* 1 causes a bug on chrome 🤷‍♂️ */
        @apply bg-opacity-40;
        @apply visible;
    }
    .gl {
        /*glass*/
        border: none;
        backdrop-filter: blur(var(--glass-blur, 40px));
        background-color: transparent;
        background-image: linear-gradient(
                135deg,
                rgb(255 255 255 / var(--glass-opacity, 30%)) 0%,
                rgb(0 0 0 / 0%) 100%
            ),
            linear-gradient(
                var(--glass-reflex-degree, 100deg),
                rgb(255 255 255 / var(--glass-reflex-opacity, 10%)) 25%,
                rgb(0 0 0 / 0%) 25%
            );
        box-shadow: 0 0 0 1px
                rgb(255 255 255 / var(--glass-border-opacity, 10%)) inset,
            0 0 0 2px rgb(0 0 0 / 5%);
        text-shadow: 0 1px rgb(0 0 0 / var(--glass-text-shadow-opacity, 5%));
    }
</style>
