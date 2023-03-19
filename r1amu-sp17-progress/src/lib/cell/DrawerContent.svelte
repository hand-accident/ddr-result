<script>
    let className;
    export { className as class };
    export let checked;
</script>

<div class="c {className}" class:checked>
    <slot />
</div>

<style lang="postcss" module>
    .c {
        /*drawer-content*/
        @apply transition-all duration-300 ease-in-out;
        direction: ltr;
        height: inherit;
        @apply z-0 col-start-1 row-start-1 overflow-y-auto;
    }
    .checked {
        /*drawer-content (toggle checked)*/
        @apply -translate-x-2;
    }
</style>
