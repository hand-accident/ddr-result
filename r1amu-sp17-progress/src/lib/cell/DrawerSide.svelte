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
        /* drawer-side*/
        direction: ltr;
        @apply col-start-1 row-start-1 grid max-h-screen overflow-x-hidden;
    }
    .checked {
        /* drawer-side (toggle checked)*/
        @apply overflow-y-auto overflow-x-hidden isolate;
    }
</style>
