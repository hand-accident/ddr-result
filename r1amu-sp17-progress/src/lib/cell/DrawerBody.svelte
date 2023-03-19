<script>
    let className;
    export { className as class };
    export let checked;
</script>

<div class="c {!checked ? 'd' : ''} {className}" class:checked>
    <slot />
</div>

<style lang="postcss" module>
    .c {
        /* drawer-overlay + * */
        @apply transition-all duration-300 ease-in-out;
        @apply justify-self-end;
        @apply z-10 col-start-1 row-start-1 transform;
    }
    .checked {
        /* drawer-overlay + *  (toggle checked)*/
        @apply translate-x-0;
    }
    .d {
        /*drawer-overlay + * (toggle not checked)*/
        @apply translate-x-full;
    }
</style>
